import React from 'react';
import ChatShort from './ChatShort.jsx';
import Chat from './Chat.jsx';
import ListGroup from "react-bootstrap/es/ListGroup";
import ListGroupItem from "react-bootstrap/es/ListGroupItem";
import FormGroup from "react-bootstrap/es/FormGroup";
import Button from "react-bootstrap/es/Button";
import ControlLabel from "react-bootstrap/es/ControlLabel";
import FormControl from "react-bootstrap/es/FormControl";
import Col from "react-bootstrap/es/Col";
import Modal from "react-bootstrap/es/Modal";
import bindActionCreators from "redux/es/bindActionCreators";
import connect from "react-redux/es/connect/connect";
import {fetchChats} from "../actions/chats.jsx";
import {openChat} from "../actions/chats.jsx";
import {closeChat} from "../actions/chats.jsx";

class ChatListComponent extends React.Component {

    componentDidMount() {
        this.props.fetchChats()
    };


    render() {
        const list = this.props.chatList.map(
            id => <ListGroupItem key={ id } onClick={ this.props.openChat.bind(this, id) }>
                <ChatShort
                    id={ id }
                />
            </ListGroupItem>
        );
        return (
            <div>
                <Col xs={12} md={8}>
                    <div>
                    <ControlLabel> Your chats </ControlLabel>
                    </div>

                    {/*<div>*/}
                    {/*<Button type="submit">*/}
                        {/*Create new chat->*/}
                    {/*</Button>*/}
                    {/*</div>*/}

                    { this.props.isLoading ? <div>Loading...</div> : <div></div> }
                    <ListGroup>
                        { list }
                    </ListGroup>
                </Col>

                <Modal show={ this.props.isChatOpened } onHide={ this.props.closeChat }>
                    <Modal.Header closeButton>
                        <Modal.Title>{ this.props.currentChatTitle }</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <Chat id={ this.props.currentChatId }/>
                    </Modal.Body>
                    <Modal.Footer>
                        {/*<Button onClick={this.close}>Close</Button>*/}
                    </Modal.Footer>
                </Modal>
            </div>
        );
    }
}

const mapStateToProps = state => ({
    chatList: state.chats.chatList,
    isLoading: state.chats.isLoading,
    isChatOpened: state.chats.isChatOpened,
    currentChatId: state.chats.currentChatId,
    currentChatTitle: state.chats.currentChatId ? state.chats.chats[state.chats.currentChatId].title : ''
});

const mapDispatchToProps = dispatch => ({
    ...bindActionCreators({ fetchChats, openChat, closeChat }, dispatch),
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(ChatListComponent);