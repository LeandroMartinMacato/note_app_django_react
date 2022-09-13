import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { ReactComponent as ArrowLeft } from "../assets/arrow-left.svg";

export default function NotePage() {
	let noteId = useParams();
	let navigate = useNavigate();
	let [note, setNote] = useState(null);

	useEffect(() => {
		getNote();
		// eslint-disable-next-line react-hooks/exhaustive-deps
	}, [noteId]);

	let getNote = async () => {
		let response = await fetch(`/api/note/${noteId.id}`);
		let data = await response.json();
		setNote(data);
	};

	let updateNote = async () => {
		await fetch(`/api/note/${noteId.id}/update`, {
			method: "PUT",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(note),
		});
	};

	let deleteNote = async () => {
		await fetch(`/api/note/${noteId.id}/delete`, {
			method: "DELETE",
			headers: {
				"Content-Type": "application/json",
			},
		});
		navigate("/");
	};

	let handleSubmit = () => {
		updateNote();
		navigate("/");
	};

	return (
		<div className="note">
			<div className="note-header">
				<h3>
					<ArrowLeft onClick={handleSubmit} />
				</h3>
				<button onClick={deleteNote}> Delete </button>
			</div>
			<textarea
				onChange={(e) => {
					setNote({ ...note, body: e.target.value }); //update state onChange
				}}
				defaultValue={note?.body}
			></textarea>
		</div>
	);
}
