import React, { Component } from "react";
import axios from "axios";

export default class MainComponent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      age: null,
    };
  }

  componentDidMount() {
    axios.get(`https://jsonplaceholder.typicode.com/posts`).then((res) => {
      const currentTime = res.data;
      console.log(currentTime);
      this.setState({ currentTime: currentTime[0].body });
    });
  }

  render() {
    return (
      <div>
        <p> {this.state.currentTime}</p>
      </div>
    );
  }
}
