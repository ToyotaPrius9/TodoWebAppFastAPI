import React from 'react';
import TodoList from './TodoList';
import Title from './Title'; 
import Me from './me';
import BackgroundMusic from './me'; 
import './App.css';

function App() {
  return (
    <div className="App">
      <Title />
      <TodoList />
      <Me />
      <BackgroundMusic /> 
    </div>
  );
}

export default App;