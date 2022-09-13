<template>
  <el-carousel :interval="4000" type="card" height="380px" class = "cardsClass">
    <el-carousel-item  class = "userCardItem" key = 1 shadow="always">
      <el-card class="userCardClass">
        <el-row class = "userCardRow">
          <el-col :span="12" class = "userForm1Col">
              <user-form-1/>
          </el-col>

          <el-col :span="12" class = "userForm2Col">
              <user-form-2/>
          </el-col>
        </el-row>
      </el-card>
    </el-carousel-item>

     
    <el-carousel-item class = "managerCardItem" key = 2 shadow="always">
      <el-card class="managerCardClass">
        <el-row class = "managerCardRow">
          <el-col :span="12" class = "managerForm1Col">
              <manager-form-1/>
          </el-col>

          <el-col :span="12" class = "managerForm2Col">
              <manager-form-2/>
          </el-col>
          
        </el-row>
      </el-card>
    </el-carousel-item>


    <el-carousel-item class = "storeCardItem" key = 3 shadow="always">
      <el-card class="storeCardClass">
        <el-row class = "storeCardRow">
          <el-col :span="12" class = "storeForm1Col">
              <store-form-1/>
          </el-col>

          <el-col :span="12" class = "storeForm2Col">
              <store-form-2/>
          </el-col>
          
        </el-row>
      </el-card>
    </el-carousel-item>


  </el-carousel>
</template>

<script>
import userForm1 from './userForm1.vue'
import userForm2 from './userForm2.vue'
import userCard from './userCard.vue'
import storeForm1 from './storeForm1.vue'
import storeForm2 from './storeForm2.vue'
import managerForm1 from './managerForm1.vue'
import managerForm2 from './managerForm2.vue'

export default {
  name: 'cards',
  components: {
    userForm1,
    userForm2,
    storeForm1,
    storeForm2,
    managerForm1,
    managerForm2,
    userCard,
  }
}
</script>

<style>

.cardsClass {
  background-color: #f8d76c;
  border-radius: 20px;
}

.el-carousel__item:nth-child(2n){
  background-color:   #fdf9e7;
  border-radius: 20px;
  width: 660px;
  height: 330px;
  margin-left: 90px;
  margin-top:30px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.07), 
                0 2px 4px rgba(0,0,0,0.07), 
                0 4px 8px rgba(0,0,0,0.07), 
                0 8px 16px rgba(0,0,0,0.07),
                0 16px 32px rgba(0,0,0,0.07), 
                0 32px 64px rgba(0,0,0,0.07);
  
}

.el-carousel__item:nth-child(2n + 1) {
  /* background-color: white; */
  background-color:   #fdf9e7;
  border-radius: 20px;
  width: 660px;
  height: 330px;
  margin-left: 90px;
  margin-top:30px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.07), 
                0 2px 4px rgba(0,0,0,0.07), 
                0 4px 8px rgba(0,0,0,0.07), 
                0 8px 16px rgba(0,0,0,0.07),
                0 16px 32px rgba(0,0,0,0.07), 
                0 32px 64px rgba(0,0,0,0.07);
  
}

</style>
