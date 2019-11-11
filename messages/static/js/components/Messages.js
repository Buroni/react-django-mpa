import React from 'react';
import ReactDOM from 'react-dom';
import { Message } from './Message';

export class Messages extends React.Component {
    render() {
    	const p = this.props;
        return p.messages.map(msg => <Message key={msg.id} message={msg}/>);
    }
}


