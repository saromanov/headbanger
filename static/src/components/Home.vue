<template>
  <div class="container">
   <span v-bind:title="message"> Hello!
   </span>
   {{message}}
   <div id="app-new-branch">
    <p>Create a new branch</p>
    <input type="text" v-model="branch_name" />
    <button v-on:click="createBranch">Create</button>
  </div>
   <div class="branches" v-if="active_branches.length">
        <p> List of active branches </p>
        <tr v-for="branch in active_branches" v-bind:key="index">
          <label>
              <input
                type="checkbox"
                v-model="active_branches_svd"
                v-on:change="listBranchChecked"
                :checked="active_branches_svd.indexOf(+branch.name)>-1"
                :value="branch.name"/>
                {{branch.name}}
                </label>
        </tr>
        <br>
        <button v-if="active_branches_svd.length" v-on:click="deleteBranches"> Delete </button>
   </div>
  </div>
</template>

<script>
'use strict'
import axios from 'axios';

export default {
  data: function() {
    return {
      message: '',
      branch_name:'',
      active_branches:[],
      active_branches_svd:[],
    }
  },
  methods: {
    createBranch: function() {
      const path = 'http://localhost:5000/api/branches';
      axios.post(path, {
        name: this.branch_name,
      }).then((res) => {
        this.getActiveBranches();
      }).catch((error) => {
        console.error(error);
      })
    },
    getActiveBranches: function() {
      const path = 'http://localhost:5000/api/branch_names';
      axios.get(path)
        .then((res) => {
          console.log(res.data.branches);
          this.active_branches = res.data.branches;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    listBranchChecked: function(){
      if(this.active_branches_svd.length == 0) {
        return
      }
    },
    deleteBranches: function(){
      const path = 'http://localhost:5000/api/branches';
      axios.delete(path, {
        data: {
          branches: this.active_branches_svd,
        }
      }).then((res) => {
          this.getActiveBranches();
          console.log(res.data.branches);
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

.branches {
  position: relative;
  width:100px;
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
