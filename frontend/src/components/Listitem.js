import React from "react";
import { Link } from "react-router-dom";

export default function ListItem({ note }) {
	return (
		<Link to={`/note/${note.id}`}>
			<div className="notes-list-item">
				<h3> {note.body} </h3>
			</div>
		</Link>
	);
}
