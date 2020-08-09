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
    <div class="search-commit" v-if="Object.keys(active_branch_commits).length > 0">
        <input type="text" placeholder="search commits" v-model="search_commit" v-on:keyup="showSearchedCommits" />
    </div>
    <p> Select branch: </p>
    <select v-model="selected_branch" :required="true" v-on:change="loadCommits">
      <option v-bind:value="branch.name" v-for="branch in active_branches" v-bind:key="branch" >{{branch.name}}</option>
    </select>
    <button v-if="Object.keys(active_branch_commits).length> 0" v-on:click="loadCommits"> Обновить </button>
    <br>
     <div class="working-branch-commits">
      <tr v-for="commit of Object.keys(active_branch_commits)" v-bind:key="commit.id">
        <div class="commit-card" v-on:click="commitPopup(commit)">
          <div class ="commit-id">
            {{commit}}
          </div>
          <div class="commit-date">
            {{active_branch_commits[commit].committed_datetime}}
          </div>
          <div class="commit-author">
            ({{active_branch_commits[commit].author}})
          </div>
          <div class="commit-name">
            {{active_branch_commits[commit].message}}
          </div>
        </div>
        <br>
      </tr>
   </div>
   <div class="commit-changes">
      <tr v-for="file of Object.keys(commit_changes)" v-bind:key="file">
        {{file}} <br>

      </tr>
   </div>
  </div>
   <div class="commit-filters" v-if="Object.keys(active_branch_commits).length > 0">
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
   <div id="commit-info" class="popup" v-bind:style="{ display: computedCommitPopupDisplay }">
      This is a test message
      <div class="cancel" onclick="closePopup();"></div>
   </div>
  </div>
</template>

<script>
'use strict'
import axios from 'axios';

export default {
  data: function() {
    return {
      active_branches:[],
      active_branch_commits_authors:[],
      active_branches_svd:[],
      active_branch_commits:{},
      branch_name:'',
      commit_changes:{},
      commit_popup_display:'none',
      message: '',
      selected_branch:'',
      search_commit:'',

    }
  },
  computed: {
    computedCommitPopupDisplay: function () {
      return this.commit_popup_display;
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
          this.active_branches = res.data.branches;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    // loading commits by the branch
    loadCommits: function(){
      const path = 'http://localhost:5000/api/commits?branch_name=' + this.selected_branch;
      this.active_branches_svd.push(45);
      axios.get(path).then((res) => {
          var values = res.data.commits;
          let commits = {}
          for (let index = 0; index < values.length; index++) {
             let key = values[index].id;
             commits[key] = values[index];
          }
          this.active_branch_commits = Object.assign({}, this.active_branch_commits, commits);
          this.active_branch_commits_authors = res.data.authors;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    // showing of commit popup with info about commit
    commitPopup: function(commit_id){
      this.commit_popup_display = 'relative';
      let data = this.active_branch_commits[commit_id];
      if(data !== undefined) {

      }
    },
    showSearchedCommits: function(){
      if(this.search_commit.length == 0) {
        this.loadCommits();
        return;
      }
      this.active_branch_commits = this.active_branch_commits.filter((x) => {
        console.log("TOTAL: ", x.stats);
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
  color:dodgerblue;
  text-align: left;
}
.commit-name {
  text-align:left;
  font-size: 20px;
  font-family:'Times New Roman', Times, serif;
}

.commit-author {
  text-align: left;
  font-size: 17px;
}
.commit-id {
  text-align: left;
  font-size: 12px;
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

.popup {
    position:fixed;
    top:0px;
    left:0px;
	  bottom:0px;
	  right:0px;
    margin:auto;
    width:200px;
    height:150px;
    font-family:verdana;
    font-size:13px;
    padding:10px;
    background-color:rgb(240,240,240);
    border:2px solid grey;
    z-index:100000000000000000;
}

.cancel {
    display:relative;
    cursor:pointer;
    margin:0;
    float:right;
    height:10px;
    width:14px;
    padding:0 0 5px 0;
    background-color:red;
    text-align:center;
    font-weight:bold;
    font-size:11px;
    color:white;
    border-radius:3px;
    z-index:100000000000000000;
}

.cancel:hover {
    background:rgb(255,50,50);
}
</style>
