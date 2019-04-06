<template>
  <div class="wrapper">
    <div class="game">
      <div
        id="NW"
        class="cell"
        v-bind:class="PlayedClasses('NW')"
        v-on:click="CrossesMove('NW')"
      ></div>
      <div
        id="N"
        class="cell"
        v-bind:class="PlayedClasses('N')"
        v-on:click="CrossesMove('N')"
      ></div>
      <div
        id="NE"
        class="cell"
        v-bind:class="PlayedClasses('NE')"
        v-on:click="CrossesMove('NE')"
      ></div>
      <div
        id="W"
        class="cell"
        v-bind:class="PlayedClasses('W')"
        v-on:click="CrossesMove('W')"
      ></div>
      <div
        id="C"
        class="cell"
        v-bind:class="PlayedClasses('C')"
        v-on:click="CrossesMove('C')"
      ></div>
      <div
        id="E"
        class="cell"
        v-bind:class="PlayedClasses('E')"
        v-on:click="CrossesMove('E')"
      ></div>
      <div
        id="SW"
        class="cell"
        v-bind:class="PlayedClasses('SW')"
        v-on:click="CrossesMove('SW')"
      ></div>
      <div
        id="S"
        class="cell"
        v-bind:class="PlayedClasses('S')"
        v-on:click="CrossesMove('S')"
      ></div>
      <div
        id="SE"
        class="cell"
        v-bind:class="PlayedClasses('SE')"
        v-on:click="CrossesMove('SE')"
      ></div>
    </div>
  </div>
</template>

<script>
const squares = ["NW", "N", "NE", "W", "C", "E", "SW", "S", "SE"];
const wins = [
  ["NW", "N", "NE"],
  ["W", "C", "E"],
  ["SW", "S", "SE"],
  ["NW", "W", "SW"],
  ["N", "C", "S"],
  ["NE", "E", "SE"],
  ["NW", "C", "SE"],
  ["SW", "C", "NE"]
];
const drawDelay = 750;

export default {
  name: "TicTacToe",
  data() {
    return {
      start: null,
      available: [],
      crosses: [],
      noughts: []
    };
  },
  created() {
    this.Init();
  },
  methods: {
    PlayedClasses(square) {
      var result = [];
      if (this.crosses.includes(square)) {
        result.push("cross");
      } else if (this.noughts.includes(square)) {
        result.push("nought");
      }
      return result;
    },
    Init() {
      this.start = null;
      this.available = JSON.parse(JSON.stringify(squares));
      this.crosses = [];
      this.noughts = [];
    },
    Reset(timestamp) {
      if (this.start === null) {
        this.start = timestamp;
      }
      if (timestamp - this.start < drawDelay) {
        window.requestAnimationFrame(this.Reset);
        return;
      }

      this.start = null;
      this.Init();
    },
    PlayMove(playerSquares, square) {
      var index = this.available.indexOf(square);
      if (index === -1 || this.start != null) {
        return;
      }
      this.available = this.available.filter(a => a !== square);
      playerSquares.push(square);
    },
    CheckWin(squares, next) {
      return wins.some(win =>
        win.every(s => squares.includes(s) || (!!next && next === s))
      );
    },
    CrossesMove(square) {
      this.PlayMove(this.crosses, square);
      if (this.CheckWin(this.crosses)) {
        this.$emit("win");
        window.requestAnimationFrame(this.Reset);
      } else if (this.available.length === 0) {
        this.$emit("draw");
        window.requestAnimationFrame(this.Reset);
      } else {
        window.requestAnimationFrame(this.NoughtsMove);
      }
    },
    //CPU Player Logic
    PickMove(moves, prop) {
      return moves.length > 0
        ? moves[Math.floor(Math.random() * moves.length)][prop]
        : null;
    },
    GetMustPlayMove(squaresToPlay) {
      var mustPlay = squaresToPlay.filter(win => win.length === 1);
      var toWin = mustPlay.filter(win => this.CheckWin(this.noughts, win[0]));
      var toBlock = mustPlay.filter(win => this.CheckWin(this.crosses, win[0]));
      return this.PickMove(toWin, 0) || this.PickMove(toBlock, 0);
    },
    GetCanPlayMove(squaresToPlay) {
      var canPlay = this.available.map(s => {
        return { square: s, value: 0 };
      });
      squaresToPlay
        .filter(win => win.length !== 1)
        .map(win => {
          win.forEach(s => {
            canPlay.find(p => {
              return p.square === s;
            }).value++;
          });
        });
      canPlay
        .sort((a, b) => {
          return a.value - b.value;
        })
        .reverse();
      var bestMoves = canPlay.filter(s => s.value === canPlay[0].value);
      return this.PickMove(bestMoves, "square");
    },
    GetNoughtsMoves() {
      return wins
        .map(win => {
          return win.filter(
            s => this.available.includes(s) && !this.crosses.includes(s)
          );
        })
        .filter(win => win.length > 0)
        .sort((a, b) => a.length - b.length);
    },
    NoughtsMove(timestamp) {
      if (this.start === null) {
        this.start = timestamp;
      }
      if (timestamp - this.start < drawDelay) {
        window.requestAnimationFrame(this.NoughtsMove);
        return;
      }

      this.start = null;
      var squaresToPlay = this.GetNoughtsMoves();
      var square =
        this.GetMustPlayMove(squaresToPlay) ||
        this.GetCanPlayMove(squaresToPlay);
      this.PlayMove(this.noughts, square);
      if (this.CheckWin(this.noughts)) {
        this.$emit("lose");
        window.requestAnimationFrame(this.Reset);
      } else if (this.available.length === 0) {
        this.$emit("draw");
        window.requestAnimationFrame(this.Reset);
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.wrapper {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  user-select: none;
  padding: 1em;
}

.game {
  width: 500px;
  height: 500px;
  position: relative;
  font-size: 0;
}

.cell {
  border: 1px solid;
  float: left;
  width: 32.9%;
  height: 32.9%;
  font-size: 100px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.cross {
  background-color: #11aa11;
}
.cross::after {
  content: "X";
}
.nought {
  background-color: #880808;
}
.nought::after {
  content: "O";
}
</style>
