<template>
  <div class="base">
    <Todo></Todo>
  </div>
</template>


<script>
  import Todo from './todo/Todo'

  export default {
    name: 'App',
    components: {
      Todo
    }
  }
</script>


<style>
  html, body {
    margin: 0;
    height: 100%;
  }

  .base {
    margin: 0;
    background-color: rgb(0, 121, 191);
    font-family: sans-serif;
    font-size: 14px;
    display: grid;
    grid-gap: 10px;
    height: 100%;
  }
</style>
