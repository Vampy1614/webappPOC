var React = require('react');

var HomePage=React.createClass({
	render:function(){
		return(
			<table className="table">
				<thead>
					<tr>
						<th>#</th>
						<th>FirstName</th>
						<th>LastName</th>
						<th>Username</th>
					</tr>
				</thead>
				<tbody id="user-data-container">
				
				</tbody>
			</table>	
		);
	}
		
});
module.exports=HomePage;