import React, { useState } from "react";
import * as firebase from "firebase/app";
// import "firebase/auth";

export default function Login(props) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  return (
    <form
      onSubmit={(event) => {
        firebase
          .auth()
          .signInWithEmailAndPassword(email, password)
          .catch(function (error) {
            // Handle Errors here.
            console.log(error.code);
            alert(error.message);
            // ...
          });

        event.preventDefault();
      }}
    >
      <input
        type="text"
        name="email"
        placeholder="E-mail"
        value={email}
        onChange={(event) => {
          setEmail(event.target.value);
        }}
      />
      <input
        type="password"
        name="password"
        placeholder="Password"
        value={password}
        onChange={(event) => {
          setPassword(event.target.value);
        }}
      />
      <input type="submit" name="submit" value="submit" />
    </form>
  );
}
