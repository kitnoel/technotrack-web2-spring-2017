import React from 'react';
import Nav from "react-bootstrap/es/Nav";
import NavItem from "react-bootstrap/es/NavItem";
import Col from "react-bootstrap/es/Col";
import Row from "react-bootstrap/es/Row";
import TabContainer from "react-bootstrap/es/TabContainer";
import TabContent from "react-bootstrap/es/TabContent";
import TabPane from "react-bootstrap/es/TabPane";
import ChatList from "./ChatList.jsx";
import PostList from "./PostList.jsx";


class MenuComponent extends React.Component {
    render() {
        return (
            <div>
            <TabContainer id="left-tabs-example" defaultActiveKey="feed">
                <Row className="clearfix">
                    <Col sm={2}/>
                    <Col sm={2}>
                        <Nav bsStyle="pills" stacked>
                            {/*<NavItem eventKey="first">*/}
                                {/*Personal page*/}
                            {/*</NavItem>*/}
                            <NavItem eventKey="second">
                                Messages
                            </NavItem>
                            <NavItem eventKey="feed">
                                Feed
                            </NavItem>
                        </Nav>
                    </Col>
                    <Col sm={8}>
                        <TabContent animation>
                            {/*<TabPane eventKey="first">*/}
                                {/*{this.props.users}*/}
                            {/*</TabPane>*/}
                            <TabPane eventKey="second">
                                <ChatList />
                            </TabPane>
                            <TabPane eventKey="feed">
                                <PostList />
                            </TabPane>
                        </TabContent>
                    </Col>
                </Row>
            </TabContainer>
            </div>
        );
    }
}

export default MenuComponent;