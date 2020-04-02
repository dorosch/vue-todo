<template>
  <div class="item">
    {{ item.text }}
  </div>
</template>


<script>
  export default {
    name: 'TodoItem',
    props: {
      item: Object
    }
  }
</script>


<style>
  .item {
    cursor: move;
    background-color: white;
    border-radius: 3px;
    box-shadow: 0 1px 0 rgba(9,30,66,.25);
    padding: 10px;
    margin-top: 5px;
  }

  .item i {
    cursor: pointer;
  }
</style>
