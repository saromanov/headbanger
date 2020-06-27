<template>
  <div id="app">
   <span v-bind:title="message"> Hello!
   </span>
   <div id="app-new-branch">
    <p>Create a new branch</p>
    <input v-model="branch_name">
    <button v-on:click="createBranch">Create</button>
  </div>
   <div class="branches" v-if="active_branches.length">
      <tbody>
        <p> List of active branches> </p>
        <tr v-for="branch in active_branches" v-bind:key="index">
          <td>{{ branch.name }}</td>
        </tr>
      </tbody>
   </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'app',
  data () {
    return {
      message: new Date(),
      branch_name:'',
      active_branches:[{name: "A", index:1},{name: "B", index:2}],
    }
  },
  methods: {
    createBranch:() => {
      console.log('Create');
    },
    getActiveBranches: (req) => {
      const path = 'http://localhost:5000/api/data';
      axios.get(path)
        .then((res) => {
          this.active_branches = res.data.branches;
        })
        .catch((error) => {
          console.error(error);
        });
    }
  },
  created() {
    this.getActiveBranches();
  },

}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  text-anchor: middle;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
