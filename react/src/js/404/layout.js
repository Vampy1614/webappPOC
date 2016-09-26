var React=require('react');
var Router = require('react-router');
var Link = Router.Link;
var NotFoundPage=React.createClass({
	
	render:function(){
		return(
			<div>
				<h1>Oops!!! Page not found!!</h1>
				<Link to="login">Go to login page</Link>
			</div>		
		
		
		);
		
	}
	
	
	
	
});
module.exports=NotFoundPage;