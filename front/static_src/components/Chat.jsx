import React from 'react';
import Message from './Message.jsx';
import ListGroup from "react-bootstrap/es/ListGroup";
import ListGroupItem from "react-bootstrap/es/ListGroupItem";
import FormGroup from "react-bootstrap/es/FormGroup";
import Button from "react-bootstrap/es/Button";
import ControlLabel from "react-bootstrap/es/ControlLabel";
import FormControl from "react-bootstrap/es/FormControl";
import Col from "react-bootstrap/es/Col";
import connect from "react-redux/es/connect/connect";
import bindActionCreators from "redux/es/bindActionCreators";
import {closeChat} from "../actions/chats.jsx";
import {fetchChat} from "../actions/chats.jsx";
import {sendMessage} from "../actions/chats.jsx";

class ChatComponent extends React.Component {
    state = {
        formContent: ''
    };

    handleChange = (e) => {
        this.setState({ formContent: e.target.value });
    };

    sendMessage = () => {
        this.props.sendMessage({content: this.state.formContent, chat: this.props.id});
    };

    componentDidMount() {
        this.props.fetchChat(this.props.id);
    }

    render() {
        const list = this.props.messageList.map(
            id => <ListGroupItem key={ id }>
                <Message
                    id={ id }
                />
            </ListGroupItem>
        );
        return (
            <div>
                <Col xs={12} md={8}>
                    <FormGroup>
                        <ControlLabel>{ this.props.title }</ControlLabel>
                    </FormGroup>

                    <FormGroup controlId="formControlsTextarea">
                        {/*<ControlLabel>Say something:</ControlLabel>*/}
                        <FormControl componentClass="textarea" placeholder="textarea" onChange={ this.handleChange } />
                    </FormGroup>

                    <Button type="submit" onClick={ this.sendMessage }>
                        Send
                    </Button>

                    <ListGroup>
                        { list }
                    </ListGroup>
                </Col>
            </div>
        );
    }
}

const mapStateToProps = (state, props) => {
    console.log(state.chats.chatMessageList);
    console.log(props.id);
    return {
        messageList: state.chats.currentChatMessagesList,
        isLoading: state.chats.isChatLoading
    };
};

const mapDispatchToProps = dispatch => ({
    ...bindActionCreators({ fetchChat, closeChat, sendMessage }, dispatch),
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(ChatComponent);
