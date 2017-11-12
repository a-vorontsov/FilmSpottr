import React, { Component } from 'react';
import './App.css';
import MapDisplay from './components/MapDisplay.js'

export default class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="mapDisplay">
          <MapDisplay className="mapView" />
        </div>
      </div>
    );
  }
}
