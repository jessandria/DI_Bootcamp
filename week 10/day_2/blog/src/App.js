import logo from './logo.svg';
import './App.css';

const charactersJson = {
  "people": [
    {
      "id" : "1",
      "name": "Luke Skywalker",
      "height": "172",
      "mass": "77",
      "hair_color": "blond",
    },
    {
      "id" : "2",
      "name": "C-3PO",
      "height": "167",
      "mass": "75",
      "hair_color": "n/a",
    },
    {
      "id" : "3",
      "name": "R2-D2",
      "height": "96",
      "mass": "32",
      "hair_color": "n/a",
    }
  ]
}

const characters = JSON.parse(JSON.stringify(charactersJson));

function App() {
  return (
    <div className='people'>
      <h1>In the App.js</h1>
      {
        characters.people.map(item => (
          <ul>
            <li>{item.name}</li>
            <li>{item.height}</li>
            <li>{item.hair_color}</li>
          </ul>
        ))
      }
    </div>
  );
}

export default App;
