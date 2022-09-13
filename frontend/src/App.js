import { BrowserRouter, Routes, Route, useParams } from "react-router-dom";

import "./App.css";
import Header from "./components/Header.js";
import NotesListPage from "./pages/NotesListPage.js";
import NotePage from "./pages/NotePage.js";

function App() {
	return (
		<BrowserRouter>
			<div className="container dark">
				<div className="app">
					<Header />
					<Routes>
						<Route path="/" exact element={<NotesListPage />} />
						<Route path="/note/:id" element={<NotePage />} />
					</Routes>
				</div>
			</div>
		</BrowserRouter>
	);
}

export default App;
