<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" />
    <TicTacToe 
      v-on:win="wins++"
      v-on:draw="draws++"
      v-on:lose="loses++" />
    <Score 
      v-bind:wins="wins"
      v-bind:draws="draws"
      v-bind:loses="loses" />
  </div>
</template>

<script>
import TicTacToe from "./components/TicTacToe.vue";
import Score from "./components/Score.vue";

export default {
  name: "app",
  data() {
    return {
      wins: 0,
      draws: 0,
      loses: 0
    };
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
  margin-top: 60px;
}
</style>
