import React, { Component } from "react";
import axios from "axios";
import Form from "react-bootstrap/Form";
import Container from "react-bootstrap/Container";
import Button from "react-bootstrap/Button";

export default class MyForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      kimlik_no: "1234",
      ad_soyad: "hasan demirkiran",
      aylik_gelir: "3000-4999TL",
      telefon: "0543",
      ikamet_ili: "34",
      final_score: "0",
    };
  }

  mySubmitHandler = (event) => {
    event.preventDefault();
    let kimlik_no = this.state.kimlik_no;
    if (!Number(kimlik_no)) {
      alert("Kimlik no yanlis girildi");
    }
    axios
      .get(`http://127.0.0.1:5000/showScore`, {
        params: {
          kimlik_no: this.state.kimlik_no,
        },
      })
      .then((response) => {
        this.setState({ final_score: response.data });
      });
  };

  myChangeHandler = (event) => {
    let nam = event.target.name;
    let val = event.target.value;
    this.setState({ [nam]: val });
  };

  // here I will be creating my options dynamically
  createOptionItems() {
    let items = [];
    for (let i = 1; i <= 81; i++) {
      items.push(<option>{i}</option>);
    }
    return items;
  }

  render() {
    return (
      <Container>
        <h2 style={{ marginBottom: "3rem" }}>SKOR HESAPLAMA UYGULAMASI</h2>
        <Form onSubmit={this.mySubmitHandler}>
          <Form.Group controlId="exampleForm.ControlInput1">
            <Form.Label>Kimlik No</Form.Label>
            <Form.Control type="number" placeholder="1234" />
          </Form.Group>
          <Form.Group controlId="exampleForm.ControlInput2">
            <Form.Label>Ad Soyad</Form.Label>
            <Form.Control type="string" placeholder="ahmet yilmaz" />
          </Form.Group>
          <Form.Group controlId="exampleForm.ControlSelect1">
            <Form.Label>Aylik Gelir</Form.Label>
            <Form.Control as="select">
              <option>0-2999TL</option>
              <option>3000-4999TL</option>
              <option>5000-7999TL</option>
              <option>8000-11999TL</option>
              <option>12000 ve üzeri</option>
            </Form.Control>
          </Form.Group>
          <Form.Group controlId="exampleForm.ControlInput3">
            <Form.Label>Telefon</Form.Label>
            <Form.Control type="number" placeholder="0534" />
          </Form.Group>
          <Form.Group controlId="exampleForm.ControlSelect2">
            <Form.Label>İkamet Edilen İl</Form.Label>
            <Form.Control as="select" multiple>
              {this.createOptionItems()}
            </Form.Control>
          </Form.Group>
          <Button variant="primary" type="submit">
            Hesapla
          </Button>
        </Form>
        {this.state.final_score != 0 ?? (
          <div>
            <h3>Your score is: {this.state.final_score}</h3>
          </div>
        )}
      </Container>
    );
  }
}
