<!-- personalCenter的子组件：用于展示用户的评价 -->

<!-- TODO：根据该用户的评价list，实例化rateCard2的list，并展示 -->

<template>
    <el-row class = "orderSheetRowClass">
        <el-col :span="12"><rateCard2/></el-col>
        <el-col :span="12"><rateCard2/></el-col>
    </el-row>
    <el-row class = "orderSheetRowClass">
        <el-col :span="12"><rateCard2/></el-col>
        <el-col :span="12"><rateCard2/></el-col>
    </el-row>
</template>

<script>
  import { defineComponent ,ref } from 'vue'
  import { NTag,NButton} from 'naive-ui'
  import rateCard2 from '../cards/rateCard2.vue'

  export default defineComponent({
    components: {
      NTag,
      NButton,
      rateCard2,
    },
  })

</script>