<template>
    <div>
        <el-container>
        <el-aside width="240px">
            <div class="mypage">
                <!-- マイページのトップページ -->
                <div class="mypage__side">
                    <side-bar />
                </div>
            </div>
        </el-aside>
        <el-main>
            <the-row>
                <the-column
                    v-for="i in 20" :key="i"
                    :pcsize="4"
                >
                    <img
                        src="https://1.bp.blogspot.com/-tVeC6En4e_E/X96mhDTzJNI/AAAAAAABdBo/jlD_jvZvMuk3qUcNjA_XORrA4w3lhPkdQCNcBGAsYHQ/s1048/onepiece01_luffy.png" alt="カレー"
                        class="mypage__img"
                        @click="onModal"
                    />
                </the-column>
            </the-row>
        </el-main>
        </el-container>
    </div>
</template>

<script>
import SideBar from '../../src/components/SideBar.vue'
import TheRow from '../../src/components/TheRow.vue'
import TheColumn from '../../src/components/TheColumn.vue'

export default {
    components: {
        SideBar,
        TheRow,
        TheColumn
    },
    data () {
        return {
            visible: false
        }
    },
    methods: {
        onModal() {
            this.visible = !this.visible
        }
    }
}
</script>

<style lang="sass" scoped>
.mypage
    $side-bar-width: 240px
    $main-width: calc(100% - #{$side-bar-width})
    &__side
        position: fixed
        left: 0
        top: 0
        width: $side-bar-width
        height: 100vh
        display: flex
    &__main
        width: $main-width
        display: grid
        grid-template-columns: $side-bar-width 1fr
    &__img
        flex: 0 0 calc(100% / 3)
        max-width: calc(100% / 2)
</style>