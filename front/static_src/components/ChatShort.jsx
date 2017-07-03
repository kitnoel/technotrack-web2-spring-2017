import React from 'react';
import Message from './Message.jsx';
import Panel from "react-bootstrap/es/Panel";
import connect from "react-redux/es/connect/connect";
import bindActionCreators from "redux/es/bindActionCreators";

export class ChatShortComponent extends React.Component {
    render() {
        return (
            <div>
                <Panel header={ this.props.title } bsStyle="primary">
                    {/*<Message*/}
                        {/*content={ this.props.last_message.content }*/}
                        {/*author={ this.props.last_message.author }*/}
                        {/*created={ this.props.last_message.created }*/}
                    {/*/>*/}
                </Panel>
            </div>
        );
    }
}

const mapStateToProps = (state, props) => {
    // const lastMessageId = state.chats.chats[props.id].last_message;
    // const title = state.chats.chats[props.id].title;
    // if (lastMessageId == null) {
    //     return {
    //         lastMessage: {text: '', created: ''},
    //         title
    //     };
    // }
    // const lastMessage = state.chats.messages[lastMessageId];
    // return {
    //     lastMessage,
    //     title
    // };
    return {
        title: state.chats.chats[props.id].title
    }
};

const mapDispatchToProps = dispatch => ({
    ...bindActionCreators({}, dispatch),
});

export default connect(
    mapStateToProps,
    mapDispatchToProps
)(ChatShortComponent);
