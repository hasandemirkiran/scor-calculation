import React, { useState, useEffect } from "react";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";

//imports
import MainComponent from "./components/MainComponent/MainComponent.js";
import MyForm from "./components/MyForm/MyForm.js";

const App = () => {
  return (
    <div>
      <MyForm />
    </div>
  );
};

export default App;
