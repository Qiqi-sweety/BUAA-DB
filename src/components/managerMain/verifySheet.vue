<!-- manageMainPage的子组件：展示待审核店铺卡片的组件 -->

<!-- TODO:
获取待审核店铺的信息list，并且实例化verifyCard，并展示 -->

<template>
    <el-row>
        <el-col :span="12"><verifyCard/></el-col>
        <el-col :span="12"> <verifyCard/></el-col>
    </el-row>
    
</template>

<script>
  import { defineComponent ,ref } from 'vue'
  import { NTag,NButton} from 'naive-ui'
  import verifyCard from '../cards/verifyCard.vue'

  export default defineComponent({
    components: {
      NTag,
      NButton,
      verifyCard,
    },
  })

</script>