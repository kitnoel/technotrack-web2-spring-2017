import React from 'react';
import PostList from './PostList.jsx';
import Menu from './Menu.jsx';
import ChatList from "./ChatList.jsx";
import User from "./User.jsx";
import {POSTS, CHATS} from '../Testing';


class AppComponent extends React.Component {

    render() {
        return (
            <Menu/>
        );
    }
}

export default AppComponent;