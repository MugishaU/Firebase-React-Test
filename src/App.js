import React from "react";
import * as firebase from "firebase/app";
import {
  FirebaseAuthProvider,
  FirebaseAuthConsumer
} from "@react-firebase/auth";
import { config } from "../src/firebaseConfig";
const concept = "world";
import "firebase/auth";
import "./styles/App.css";

class App extends React.Component {
  state = {};
  render() {
    return (
      <>
        <h1>New React App</h1>
        <h2>Happy Coding</h2>

        <FirebaseAuthProvider {...config} firebase={firebase}>
          <div>
            Hello <div>From Auth Provider Child 1</div>
            <FirebaseAuthConsumer>
               {({ isSignedIn, firebase }) => {
              if (isSignedIn === true) {
                return (
                  <div>
                    <h2>You're signed in 🎉 </h2>
                    <button
                      onClick={() => {
                        firebase
                          .app()
                          .auth()
                          .signOut();
                      }}
                    >
                      Sign out
                    </button>
                  </div>
                );
              } else {
                return (
                  <div>
                    <h2>You're not signed in </h2>
                    <button
                      onClick={() => {
                        firebase
                          .app()
                          .auth()
                          .signInAnonymously();
                      }}
                    >
                      Sign in anonymously
                    </button>
                  </div>
                );
              }
            }}
            </FirebaseAuthConsumer>
          </div>
          <div>Another div</div>
       </FirebaseAuthProvider>
      </>
    );
  }
}


export default App;
