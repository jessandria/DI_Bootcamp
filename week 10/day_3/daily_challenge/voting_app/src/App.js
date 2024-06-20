import React, { useState } from 'react';
import './App.css';

function App() {
  const [languages, setLanguages] = useState([
    { name: 'Php', votes: 0 },
    { name: 'Python', votes: 0 },
    { name: 'JavaScript', votes: 0 },
    { name: 'Java', votes: 0 },
  ]);

  const handleVote = (index) => {
    const newLanguages = [...languages];
    newLanguages[index].votes += 1;
    setLanguages(newLanguages);
  };

  return (
    <div className="App">
      <h1>Vote Your Language!</h1>
      {languages.map((language, index) => (
        <div className="language-box" key={index}>
          <span className="votes">{language.votes}</span>
          <span className="language-name">{language.name}</span>
          <button onClick={() => handleVote(index)}>Click Here</button>
        </div>
      ))}
    </div>
  );
}

export default App;
