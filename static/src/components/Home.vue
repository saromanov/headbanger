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
  <div class="working-branch">
    <div class="search-commit" v-if="active_branch_commits.length > 0">
        <input type="text" placeholder="search commits" v-model="search_commit" v-on:keyup="showSearchedCommits" />
    </div>
    <p> Select branch: </p>
    <select v-model="selected_branch" :required="true" v-on:change="loadCommits">
      <option v-bind:value="branch.name" v-for="branch in active_branches" v-bind:key="index" >{{branch.name}}</option>
    </select>
    <button v-if="active_branch_commits.length> 0" v-on:click="loadCommits"> Обновить </button>
    <br>
     <div class="working-branch-commits">
      <tr v-for="commit in active_branch_commits" v-bind:key="idx">
        <div class="commit-card">
          <div class="commit-date">
            {{commit.committed_datetime}}
          </div>
          ({{commit.author}})
          <div class="commit-name">
            {{commit.message}}
          </div>
        </div>
        <br>
      </tr>
   </div>
  </div>
   <div class="commit-filters" v-if="active_branch_commits.length > 0">
        <p> Filters </p>
        <tr v-for="author in active_branch_commits_authors" v-bind:key="index">
          <label>
              <input
                type="checkbox"
                v-model="active_branches_svd"
                :checked="active_branches_svd.indexOf(+author)>-1"
                :value="author"/>
                {{author}}
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
      selected_branch:'',
      search_commits:'',
      active_branches:[],
      active_branch_commits_authors:[],
      active_branches_svd:[],
      active_branch_commits:[],
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
    loadCommits: function(){
      const path = 'http://localhost:5000/api/commits?branch_name=' + this.selected_branch;
      axios.get(path).then((res) => {
          this.active_branch_commits = res.data.commits;
          this.active_branch_commits_authors = res.data.authors;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    showSearchedCommits: function(){
      if(this.search_commit.length == 0) {
        this.loadCommits();
        return;
      }
      this.active_branch_commits = this.active_branch_commits.filter((x) => {
        return x.message.indexOf(this.search_commit) > 0 ;
      });
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
  font-size: 20;
  font-family: 'Courier New', Courier, monospace;
}
.commit-date {
  font-size: 15px;
  color: burlywood;
  text-align: left;
}
.commit-name {
  text-align:left;
}

.commit-card {
  background-color: bisque;
}
.search-commit {
  height: 20px;
  text-align: center;
  color: #42b983;
}
.working-branch {
  height: 10em;
  position: relative;
  margin: 0 auto;
  width:500px;
}

.working-branch-commits {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  font-size: 20px;
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
