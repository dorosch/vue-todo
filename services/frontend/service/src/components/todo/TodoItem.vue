<template>
  <li>
    {{ item.text }}
  </li>
</template>


<script>
  export default {
    name: 'TodoItem',
    props: {
      item: Object
    }
  }
</script>
