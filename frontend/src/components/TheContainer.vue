<template>
  <div class="container">
    <slot />
  </div>
</template>

<script>
export default {}
</script>

<style lang="sass" scoped>
//まだ途中
.container
  margin: 0 auto
  width: 960px
  padding: 0 $container-padding
  @include media-breakpoint-down(lg)
    margin: 0 0
    width: 100%
</style>
