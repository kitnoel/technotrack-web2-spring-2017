import fetch from 'isomorphic-fetch';
import * as Cookies from "js-cookie";

// export const ADD_CHAT = 'ADD_CHAT';
export const LOAD_CHATS = 'LOAD_CHATS';
export const LOAD_CHATS_SUCCESS = 'LOAD_CHATS_SUCCESS';
export const LOAD_CHATS_ERROR = 'LOAD_CHATS_ERROR';
export const LOAD_CHAT = 'LOAD_CHAT';
export const LOAD_CHAT_SUCCESS = 'LOAD_CHAT_SUCCESS';
export const LOAD_CHAT_ERROR = 'LOAD_CHAT_ERROR';
export const OPEN_CHAT = 'OPEN_CHAT';
export const CLOSE_CHAT = 'CLOSE_CHAT';

export function addChat(chat) {
    return {
        type: ADD_CHAT,
        chat
    };
}

export function loadChats() {
    return {
        type: LOAD_CHATS,
    };
}

export function loadChatsSuccess(responce) {
    return {
        type: LOAD_CHATS_SUCCESS,
        responce
    };
}

export function loadChatsError() {
    return {
        type: LOAD_CHATS_ERROR,
    };
}

export function fetchChats() {
    return dispatch => {
        dispatch(loadChats());
        return fetch('/api/chats/', {
            credentials: "same-origin",
        })
            .then(responce => responce.json())
            .then(json => {console.log(json); return json;})
            .then(json => dispatch(loadChatsSuccess(json)));
    };
}

export function loadChatSuccess(responce) {
    return {
        type: LOAD_CHAT_SUCCESS,
        responce,
    };
}

export function loadChat(id) {
    return {
        type: LOAD_CHAT,
        id
    };
}

export function loadChatError() {
    return {
        type: LOAD_CHAT_ERROR,
    };
}

export function openChat(id) {
    return {
        type: OPEN_CHAT,
        id
    };
}

export function closeChat() {
    return {
        type: CLOSE_CHAT,
    };
}

export function fetchChat(id) {
    return dispatch => {
        dispatch(loadChat(id));
        return fetch('/api/messages/?chat='+id, {
            credentials: "same-origin",
        })
            .then(responce => {console.log(responce); return responce})
            .then(responce => responce.json())
            .then(json => dispatch(loadChatSuccess(json)));
    };
}

export function sendMessage(message) {
    return dispatch => {
        let formData = new FormData();
        formData.append('content', message.content);
        formData.append('chat', message.chat);
        formData.append('csrfmiddlewaretoken', Cookies.get('csrftoken'));
        return fetch('/api/messages/', {
            credentials: "same-origin",
            method: 'POST',
            body: formData
        })
            .then(() => dispatch(fetchChat(message.chat)));
    };
}
