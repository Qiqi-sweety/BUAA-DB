<template>
    <el-button size = "large" 
    style = "margin-bottom: 20px;"
    @click="showAddModal = true">添加商品</el-button>
    <el-table :data="tableData" style="width: 100%">
      <el-table-column prop = "编号" label="编号" width="200">
      </el-table-column>
      <el-table-column prop = "商品名称" label="商品名称" width="300">
      </el-table-column>
      <el-table-column prop = "商品价格" label="商品价格" width="250">
      </el-table-column>

      <el-table-column prop = "商品销量" label="商品销量" width="250">
      </el-table-column>

      <el-table-column label="商品图片" width="300">   
        <template #default="scope">
          <div style="display: flex; align-items: center">
            <el-image :src="scope.row.商品图片" style = "width: 80px;height: 80px;"/>
          </div>
        </template> 
      </el-table-column>

      <el-table-column>
        <template #default="scope">
          <el-button
            size="media"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)"
            >删除</el-button
          >
        </template>
      </el-table-column>
  </el-table>

  <n-modal
    v-model:show="showAddModal"
    preset="card"
    :style="bodyStyle"
    title="添加商品"
    style="width:500px"
    :bordered="false"
    :segmented="segmented"
    >
        <n-card
        style="width: 450px"
        :bordered="false"
        size="huge"
        role="dialog"
        aria-modal="true"
        >

       
        <el-input
          v-model="input"
          placeholder="请输入商品名称"
          size = "large"
          style = "margin-bottom: 20px;" 
        >
          <template #prefix>
            <el-icon><Goods /></el-icon>
          </template>
  
        </el-input>

        <el-input
          v-model="input"
          placeholder="请输入商品价格"
          size = "large"
          style = "margin-bottom: 30px;" 
        >
          <template #prefix>
            <el-icon><Money /></el-icon>
          </template>
  
        </el-input>

        <n-upload
            action="https://www.mocky.io/v2/5e4bafc63100007100d8b70f"
            @before-upload="beforeUpload"
            >
              <n-button size = "large"
              style = "width: 150px;margin-top: 0px;"
              >
                上传商品图片
              </n-button>
          </n-upload>       

  
        <n-button style = "margin-left:130px;margin-top: 10px;" size = "large" round type="warning">
        确认添加
        </n-button>  
    </n-card>
  </n-modal>


</template>

<script>
  import { defineComponent ,ref } from 'vue'
  import {NCard,NRate,NButton,NModal,NUpload,NInput} from 'naive-ui'

  const tableDate = [];
  export default defineComponent({
    components: {
      NCard,
      NRate,
      NButton,
      NModal,
      NUpload,
      NInput,
    },
    setup() {
      return {
        showAddModal: ref(false),
        tableData :[
        {
          编号: 1,
          商品名称: "烤黑糖波波牛乳",
          商品价格: 19,
          商品销量: 0,
          商品图片:require("@/assets/喜茶.jpg"),
        },
        {
          编号: 1,
          商品名称: "烤黑糖波波牛乳",
          商品价格: 19,
          商品销量: 0,
          商品图片:require("@/assets/喜茶.jpg"),
          // 商品图片:require("../../assets/喜茶.jpg"),
        },
      
      ]
      }
 
    }
  })
</script>
