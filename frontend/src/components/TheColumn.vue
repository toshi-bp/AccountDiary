<template>
  <div
    class="column"
    :class="[`column--is-pcsize-${pcsize}`, `column--is-spsize-${spsize}`]"
  >
    <slot />
  </div>
</template>

<script>
export default {
  props: {
    pcsize: {
      type: Number,
      default: 4
    },

    spsize: {
      type: Number,
      default: 6
    }
  }
}
</script>

<style lang="sass" scoped>
.column
  $the-width: calc(100% - 256px)
  $row-gutter: 0.5rem
  padding: 0 $row-gutter

  &--is-pcsize-2
    flex: 0 0 calc(#{$the-width} / 6)
    max-width: calc(#{$the-width} / 6)

  &--is-pcsize-3
    flex: 0 0 calc(#{$the-width} / 4)
    max-width: calc(#{$the-width} / 4)

  &--is-pcsize-4
    flex: 0 0 calc(#{$the-width} / 3)
    max-width: calc(#{$the-width} / 3)

  &--is-pcsize-6
    flex: 0 0 calc(#{$the-width} / 2)
    max-width: calc(#{$the-width} / 2)

  &--is-pcsize-12
    flex: 0 0 calc(#{$the-width} / 1)
    max-width: calc(#{$the-width} / 1)

//   &--is-spsize-4
//     @include media-breakpoint-down(756px)
//       flex: 0 0 calc(100% / 3)
//       max-width: calc(100% / 3)


//   &--is-spsize-6
//     @include media-breakpoint-down(756px)
//       flex: 0 0 calc(100% / 2)
//       max-width: calc(100% / 2)


//   &--is-spsize-12
//     @include media-breakpoint-down(756px)
//       flex: 0 0 calc(100% / 1)
//       max-width: calc(100% / 1)
</style>
