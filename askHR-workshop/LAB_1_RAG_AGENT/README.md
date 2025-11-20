# Lab 1: Knowledge base
This lab we will import knowledgebase agent that contain built-in milvus vectir db for policy pdf

### Prerequisites
- Complete Lab_0 (setup the lab environment).
- Have the `orchestrate` CLI installed and configured.
- complete LAB_1 to activate orchestrate environment. If not, run the following command

```
orchestrate env list
orchestrate env activate trial-env -a <YOUR_API_KEY>
```


This lab we will use an ADK(Agent Development Kit) to create and configurate the accounting agent. This agent allows users to chat and ask question from a document which is stored in a knowledge base within watsonx orchestrate embed vector database.

---

run the following command
```
bash import-all.sh
```
or
```
orchestrate knowledge-bases import -f policy/group_knowledge_base.yaml
orchestrate agents import -f general_agent.yaml
```


---

## Testing knowledge-base queries

you can test with following questions

- อยากทราบเกี่ยวกับคำจำกัดความของคำว่าลา
- บทบาทความรับผิดชอบของพนักงาน
- ผู้จัดการมีหน้าที่อะไร
- การลาพักร้อนต้องทำยังไงบ้าง
- เหตุผลใดบ้างที่นับเป็นการลาพักร้อน
- พฤติกรรมใดบ้างที่นับเป็นการฝ่าฝืนนโยบายของบริษัท
- ลาโดยไม่ได้รับค่าจ้างสามารถลาได้กี่ครั้ง
- อยากทราบข้อมูลสรุปของการลาคลอด