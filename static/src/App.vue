<template>
  <div id="app">
   <span v-bind:title="message"> Hello!
   </span>
   <div id="app-new-branch">
     {{ active_branches }}
    <p>Create a new branch</p>
    <input v-model="branch_name">
    <button v-on:click="createBranch">Create</button>
  </div>
   <div class="branches" v-if="active_branches.length">
        <p> List of active branches> </p>
        <tr v-for="branch in active_branches" v-bind:key="index">
          <td>{{ branch.name }}</td>
        </tr>
   </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data:() =>{
    return {
      message: new Date(),
      branch_name:'',
      active_branches:[],
    }
  },
  methods: {
    createBranch:() => {
      console.log("MESSAGE: ", this.message);
      const path = 'http://localhost:5000/api/branches';
      axios.post(path, {
        name: this.branch_name,
      }).then((res) => {
        console.log('FINE');
      }).catch((error) => {
        console.error(error);
      })
    },
    getActiveBranches: () => {
      const path = 'http://localhost:5000/api/branch_names';
      axios.get(path)
        .then((res) => {
          console.log(res.data.branches);
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
