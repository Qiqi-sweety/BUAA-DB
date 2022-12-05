<!-- manageMainPage的子组件：展示待审核店铺卡片的组件 -->

<!-- TODO:
获取待审核店铺的信息list，并且实例化verifyCard，并展示 -->

<template>
    <el-row>
        <el-col :span="12" v-for="store in info.unvalid_stores">
          <verifyCard :store="store"/>
        </el-col>
    </el-row>
    
</template>

<script setup>
import {onMounted, reactive} from "vue";

const info = reactive({
  unvalid_stores: []
})
onMounted(() => {

})
</script>