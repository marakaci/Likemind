from copy import deepcopy
from datetime import datetime

from attr import dataclass

from chat.consts import CHAT_TEXT_MESSAGE
from chat.consumers import CONSUMER_CHAT_MESSAGE, CONSUMER_USER_EVENT
from files.consts import CHAT_IMAGE_MESSAGE, CHAT_VIDEO_MESSAGE, CHAT_FILE_MESSAGE, CHAT_AUDIO_MESSAGE
from utils.constants import TIME_TZ_FORMAT

action_types = [CHAT_TEXT_MESSAGE, CHAT_IMAGE_MESSAGE, CHAT_VIDEO_MESSAGE, CHAT_FILE_MESSAGE, CHAT_AUDIO_MESSAGE]
event_types = [CONSUMER_CHAT_MESSAGE, CONSUMER_USER_EVENT]


class ActionType:
    flat_dict = None

    def __init__(self):
        self.flat_dict = {}

    def to_dict(self):
        _dict = vars(self)
        _dict['action_type'] = self.action_type()

    def to_flat_dict(self):
        if self.flat_dict:
            return self.flat_dict
        _dict = self.to_dict()
        for key, value in _dict.items():
            self._rec_to_dict_flat(key, value)
        return self.flat_dict

    def _rec_to_dict_flat(self, key, value):
        if not isinstance(value, dict):
            if key in self.flat_dict:
                print(self.flat_dict)
                raise KeyError('key {} already exists'.format(key))
            self.flat_dict[key] = value
        else:
            for key, value in value.items():
                self._rec_to_dict_flat(key, value)

    @classmethod
    def action_type(cls):
        raise NotImplementedError


@dataclass
class ChatContentMessageAction(ActionType):
    id: int
    chat_type: str
    chat: int
    owner: int
    created_at: datetime

    def to_dict(self):
        _dict = super(ChatContentMessageAction, self).to_dict()
        _dict['created_at'] = datetime.strftime(_dict['created_at'], TIME_TZ_FORMAT)
        return _dict


@dataclass
class ChatTextMessageAction(ChatContentMessageAction):
    text: str
    edited: bool
    edited_at: datetime

    def to_dict(self):
        _dict = super(ChatTextMessageAction, self).to_dict()
        _dict['edited_at'] = datetime.strftime(_dict['edited_at'], TIME_TZ_FORMAT)
        return _dict

    @classmethod
    def action_type(cls):
        return CHAT_TEXT_MESSAGE


@dataclass
class ChatImageMessageAction(ChatContentMessageAction):
    image: str

    @classmethod
    def action_type(cls):
        return CHAT_IMAGE_MESSAGE


@dataclass
class ChatVideoMessageAction(ChatContentMessageAction):
    video: str

    @classmethod
    def action_type(cls):
        return CHAT_VIDEO_MESSAGE


@dataclass
class ChatAudioMessageAction(ChatContentMessageAction):
    audio: str

    @classmethod
    def action_type(cls):
        return CHAT_AUDIO_MESSAGE


@dataclass
class ChatFileMessageAction(ChatContentMessageAction):
    file: str

    @classmethod
    def action_type(cls):
        return CHAT_FILE_MESSAGE


class WebSocketEvent:

    def __init__(self, action: ActionType, type=None):
        if type:
            if not type in event_types:
                raise ValueError('No such consumer event type')
            self.type = type
        self.action = action

    def to_dict(self):
        _dict = vars(self)
        _dict.pop('action')
        _dict['action'] = self.action.to_dict()
        _dict['action_type'] = _dict['action']['action_type']
        _dict['action'].pop('action_type')
        return _dict

    def to_dict_flat(self):
        _dict = vars(self)
        _dict.pop('action')
        _dict.update(self.action.to_flat_dict())
        return _dict
