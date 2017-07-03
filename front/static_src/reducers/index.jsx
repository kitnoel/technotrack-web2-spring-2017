import { combineReducers } from 'redux';
import posts from './posts.jsx';
import chats from './chats.jsx';

export default combineReducers({
    posts,
    chats
});
