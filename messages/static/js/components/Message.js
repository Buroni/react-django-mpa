import React from 'react';
import ReactDOM from 'react-dom';

export class Message extends React.Component {
    render() {
    	const p = this.props;
    	return <div className={"msg-box"}>
    			<h2>{ p.message.author } (Id={ p.message.id })</h2>
    			<p>{ p.message.text }</p>
    		</div>;
    }
}
