<template>
  <div id="app">
    <h1>Tic Tac Vue!</h1>
    <img alt="Vue logo" src="./assets/logo.png" />
    <Score v-bind:wins="wins" v-bind:draws="draws" v-bind:loses="loses" />
    <TicTacToe
      v-on:win="UpdateScore('wins')"
      v-on:draw="UpdateScore('draws')"
      v-on:lose="UpdateScore('loses')"
    />
  </div>
</template>

<script>
import TicTacToe from "./components/TicTacToe.vue";
import Score from "./components/Score.vue";

export default {
  name: "app",
  data() {
    return {
      wins: Number(localStorage.getItem("wins")) || 0,
      draws: Number(localStorage.getItem("draws")) || 0,
      loses: Number(localStorage.getItem("loses")) || 0
    };
  },
  methods: {
    UpdateScore(field) {
      localStorage.setItem(field, ++this[field]);
    }
  },
  components: {
    TicTacToe,
    Score
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 30px;
}
img {
  max-height: 120px;
}
</style>
