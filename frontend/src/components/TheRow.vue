<template>
  <div class="row">
    <slot />
  </div>
</template>

<style lang="sass" scoped>
.row
  $row-gutter: 0.5rem
  display: flex
  flex-wrap: wrap
  margin: 0
  justify-content: center
  align-items: center
</style>
