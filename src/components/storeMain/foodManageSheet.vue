<template>
    <el-button size = "large" 
    style = "margin-bottom: 20px;"
    @click="showAddModal = true">添加商品</el-button>
    <el-table :data="info.items" style="width: 100%" table-layout="fixed">
      <el-table-column prop = "id" label="编号">
      </el-table-column>
      <el-table-column prop = "name" label="商品名称">
      </el-table-column>
      <el-table-column prop = "price" label="商品价格">
      </el-table-column>

      <el-table-column prop = "sales" label="商品销量">
      </el-table-column>

      <el-table-column label="商品图片">
        <template #default="scope">
          <div style="display: flex; align-items: center">
            <el-image :src="`/api${scope.row.image}`" style = "width: 80px;height: 80px;"/>
          </div>
        </template> 
      </el-table-column>

      <el-table-column>
        <template #default="scope">
          <el-button
            size="default"
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
    title="添加商品"
    style="width:500px"
    :bordered="false"
  >
    <el-form
        ref="ruleFormRef"
        :model="info.new_item"
        :rules="rules"
        status-icon
        style="width: 450px;"
    >
      <el-form-item prop="name">
        <el-input
          v-model="info.new_item.name"
          placeholder="请输入商品名称"
          size = "large"
        >
          <template #prefix>
            <el-icon class="el-input__icon"><Goods /></el-icon>
          </template>
  
        </el-input>
      </el-form-item>
      <el-form-item prop="price">
        <el-input-number
          v-model="info.new_item.price"
          placeholder="请输入商品价格"
          controls-position="right"
          size = "large"
          :precision="2"
          :min="0"
          style="width: 100%"
        >
          <template #prefix>
            <el-icon class="el-input__icon"><Money /></el-icon>
          </template>
  
        </el-input-number>
      </el-form-item>
      <el-form-item prop="intro">
        <el-input
            v-model="info.new_item.intro"
            placeholder="请输入商品简介"
            :autosize="{ minRows: 3, maxRows: 4 }"
            type="textarea"
            maxlength="500"
            show-word-limit
        >
          <template #prefix>
            <el-icon class="el-input__icon"><Document /></el-icon>
          </template>

        </el-input>
      </el-form-item>
      <el-form-item prop="image">
          <el-upload
              :limit="1"
              action="/api/image/update/"
              :on-success="handleImageSuccess"
          >
              <n-button size = "large" style = "width: 150px;margin-top: 0px;">
                上传商品图片
              </n-button>
          </el-upload>
      </el-form-item>
      <el-form-item>
        <n-button style = "margin-left:130px;margin-top: 10px;" size = "large" round type="warning" @click="addItem(ruleFormRef)">
        确认添加
        </n-button>
      </el-form-item>
    </el-form>
  </n-modal>


</template>

<script setup>
import {onMounted, reactive, ref} from 'vue'
import {NButton,NModal} from 'naive-ui'
import {show_items, add_items, del_items} from "@/api/store";
import {ElMessage} from "element-plus";

const showAddModal = ref(false)
const info = reactive({
  items: [],
  new_item: {price: 0}
})
const ruleFormRef = ref()

const rules = reactive({
  name: [
    {
      required: true,
      message: '请输入商品名称',
      trigger: 'blur'
    },
    {
      max: 256,
      message: '商品名称过长，请重新输入',
      trigger: 'change'
    }
  ],
  image: [
    {
      required: true,
      message: '请上传商品图片',
      trigger: 'blur',
    },
  ],
  price: [
    {
      required: true,
      message: '请输入商品价格',
      trigger: 'blur',
    },
  ],
  intro: [
    {
      required: true,
      message: '请输入商品简介',
      trigger: 'blur',
    },
  ],
})

const handleImageSuccess = (res) => {
  console.log(res)
  info.new_item.image = res.url
}

const handleDelete = (index, row) => {
  console.log(index, row)
  del_items({
    item_id: row.id
  }).then(res => {
    let content = res.data
    console.log(content)
    ElMessage({message: content.message, type: content.hint})
    if (content.code === "200") {
      show_items().then(res => {
        let content = res.data
        console.log(content)
        info.items = []
        if (content.code === "200") {
          content.item_data.forEach(item => {
            info.items.push(item)
          })
        }
      })
    }
  })
}

const addItem = async (formEl) => {
  if (!formEl) return
  await formEl.validate((valid, fields) => {
    if (valid) {
      add_items(info.new_item).then(res => {
        let content = res.data
        console.log(content)
        ElMessage({message: content.message, type: content.hint})
        if (content.code === "200") {
          show_items().then(res => {
            let content = res.data
            console.log(content)
            info.items = []
            if (content.code === "200") {
              content.item_data.forEach(item => {
                info.items.push(item)
              })
            }
          })
        }
      })
    } else {
      ElMessage({message: "信息不完整，请继续完善", type: "error"})
    }
  })
  showAddModal.value = false
}

onMounted(() => {
  show_items().then(res => {
    let content = res.data
    console.log(content)
    info.items = []
    if (content.code === "200") {
      content.item_data.forEach(item => {
        info.items.push(item)
      })
    }
  })
})
</script>
