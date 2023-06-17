<template>
    <div class="container mt-4">
     <div class="card" align="left">
      <h2>Student Registation</h2>
                    <form>
                    <div class="form-group">
                        <label>student name</label>
                        <input type="text" v-model="student.name" class="form-control"  placeholder="Enter Student name">
                    </div>

                    <div class="form-group">
                        <label>student Address</label>
                        <input type="text" v-model="student.address" class="form-control"  placeholder="Enter Student Address">
                    </div>


                    <div class="form-group">
                        <label>Fee</label>
                        <input type="text" v-model="student.fee" class="form-control"  placeholder="Enter Student Fee">
                    </div>
                    <br>
                    <button type="submit" class="btn btn-primary"  @click="saveData()">Save</button>
                    <button type="submit" class="btn btn-warning" @click="updateData()">Update</button>

                  </form>
      </div>

<h2>Student Table</h2>
      <table class="table table-dark">
  <thead>
    <tr>
      <th scope="col">ID</th>
      <th scope="col">student Name</th>
      <th scope="col">Address</th>
      <th scope="col">Mobile</th>
      <th scope="col">Option</th>
    </tr>
  </thead>

  <tbody>
    <tr v-for="student in result" v-bind:key="student.id">

          <td>{{ student.id }}</td>
          <td>{{ student.name }}</td>
          <td>{{ student.address }}</td>
          <td>{{ student.fee }}</td>
          <td>
            <button type="button" class="btn btn-warning" @click="edit(student)">Edit</button>
            <button type="button" class="btn btn-danger"  @click="remove(student)">Delete</button>
          </td>
        </tr>

  </tbody>


</table>

    </div>

  </template>

  <script>
    import Vue from 'vue';
    import axios from 'axios';
     Vue.use(axios)
  export default {
    name: 'Student',
    data () {
      return {
        result: {},
        student:{
                   id: '',
                   name: '',
                   address: '',
                   fee: ''
        }
      }
    },
    created() {
        this.studentLoad();
    },
    mounted() {
          console.log("mounted() called.......");

      },
    methods: {
           studentLoad()
           {
                 var page = "http://127.0.0.1:8000/student";
                 axios.get(page)
                  .then(
                      ({data})=>{
                        console.log(data);
                        this.result = data;
                      }
                  );
           },

           saveData()
           {
            axios.post("http://127.0.0.1:8000/student", this.student)
            .then(
              ({data})=>{
                alert("saveddddd");
                this.studentLoad();
                 this.student.name = '';
                  this.student.address = '',
                  this.student.fee= ''
                   this.id = ''
              }
            )
           },

           edit(student)
           {
            this.student = student;

           },
           updateData()
           {
              var editrecords = 'http://127.0.0.1:8000/student/'+ this.student.id;
              axios.put(editrecords, this.student)
              .then(
                ({data})=>{
                  this.student.name = '';
                  this.student.address = '',
                  this.student.fee = ''
                  this.id = ''
                  alert("Updated!!!");
                  this.studentLoad();
                }
              );
           },

           remove(student){
             var url = `http://127.0.0.1:8000/student/${student.id}`;
             // var url = 'http://127.0.0.1:8000/api/delete/'+ student.id;
              axios.delete(url);
              alert("Deleteddd");
              this.studentLoad();
            }
      }
  }
  </script>
