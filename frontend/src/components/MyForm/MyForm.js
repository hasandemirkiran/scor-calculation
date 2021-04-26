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
          aylik_gelir: this.state.aylik_gelir,
        },
      })
      .then((response) => {
        console.log(response.data);
        this.setState({ final_score: response.data });
      });
  };

  myChangeHandler = (event) => {
    let nam = event.target.id;
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
        {this.state.final_score !== 0 ? (
          <div>
            <h3>Your score is: {this.state.final_score}</h3>
          </div>
        ) : (
          <div>
            <h3>Bilgilerinizi giriniz</h3>
          </div>
        )}
        <Form onSubmit={this.mySubmitHandler}>
          <Form.Group controlId="kimlik_no">
            <Form.Label>Kimlik No</Form.Label>
            <Form.Control
              type="number"
              placeholder="1234"
              onChange={this.myChangeHandler}
            />
          </Form.Group>
          <Form.Group controlId="ad_soyad">
            <Form.Label>Ad Soyad</Form.Label>
            <Form.Control
              type="string"
              placeholder="ahmet yilmaz"
              onChange={this.myChangeHandler}
            />
          </Form.Group>
          <Form.Group controlId="aylik_gelir">
            <Form.Label>Aylik Gelir</Form.Label>
            <Form.Control as="select" onChange={this.myChangeHandler}>
              <option>0-2999TL</option>
              <option>3000TL-4999TL</option>
              <option>5000TL-7999TL</option>
              <option>8000TL-11999TL</option>
              <option>12000TL ve üzeri</option>
            </Form.Control>
          </Form.Group>
          <Form.Group controlId="telefon">
            <Form.Label>Telefon</Form.Label>
            <Form.Control
              type="number"
              placeholder="0534"
              onChange={this.myChangeHandler}
            />
          </Form.Group>
          <Form.Group controlId="ikamet_ili">
            <Form.Label>İkamet Edilen İl</Form.Label>
            <Form.Control as="select" multiple onChange={this.myChangeHandler}>
              {this.createOptionItems()}
            </Form.Control>
          </Form.Group>
          <Button variant="primary" type="submit">
            Hesapla
          </Button>
        </Form>
      </Container>
    );
  }
}
