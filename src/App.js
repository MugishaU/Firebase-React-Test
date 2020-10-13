import React from "react";
import * as firebase from "firebase/app";
import {
  FirebaseAuthProvider,
  FirebaseAuthConsumer,
  IfFirebaseAuthed,
  IfFirebaseUnAuthed,
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
            Hello <div>From FirebaseAuthProvider</div>
            <IfFirebaseAuthed>
              {() => (
                <div>
                  <h2>You're signed in 🎉 </h2>
                  <button
                    onClick={() => {
                      firebase.app().auth().signOut();
                    }}
                  >
                    Sign out
                  </button>
                  <button
                    onClick={() => {
                      // console.log(firebase.auth().currentUser);
                      firebase
                        .auth()
                        .currentUser.getIdToken(/* forceRefresh */ true)
                        .then(function (idToken) {
                          console.log(`token: ${idToken}`);
                        })
                        .catch(function (error) {
                          console.log(error);
                        });
                    }}
                  >
                    Get Token
                  </button>
                </div>
              )}
            </IfFirebaseAuthed>
            <IfFirebaseUnAuthed>
              {({ firebase }) => (
                <div>
                  <h2>You're not signed in </h2>
                  <button
                    onClick={() => {
                      firebase.app().auth().signInAnonymously();
                    }}
                  >
                    Sign in anonymously
                  </button>
                  <button
                    onClick={async () => {
                      try {
                        const googleAuthProvider = new firebase.auth.GoogleAuthProvider();
                        await firebase
                          .auth()
                          .signInWithPopup(googleAuthProvider);
                      } catch (error) {
                        console.log(error);
                      }
                    }}
                  >
                    Sign in with Google
                  </button>
                </div>
              )}
            </IfFirebaseUnAuthed>
          </div>
          <div>Another div</div>
        </FirebaseAuthProvider>
      </>
    );
  }
}

export default App;
