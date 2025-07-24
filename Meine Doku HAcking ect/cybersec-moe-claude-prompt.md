# Claude Code Prompt: Complete Cybersecurity MoE Configuration

**IMPORTANT: Use ultrathinking for every step, employ 200 IQ reasoning, and act as a professional team of engineers, researchers, and PhDs specializing in AI, ML, MCPs, and Cybersecurity.**

## Project Overview
Configure, optimize, and deploy a production-ready quantized Cybersecurity Mixture of Experts (MoE) model using 7 RTX 4070 GPUs (12GB VRAM each) on Windows with WSL2. The system must integrate 50% MCP functionality for real-time threat intelligence and database operations.

## Phase 1: Environment Setup & GPU Clustering

### 1.1 WSL2 Configuration
```bash
# Check and enable WSL2 with GPU support
wsl --update
wsl --set-default-version 2
# Install Ubuntu 22.04 LTS
wsl --install -d Ubuntu-22.04

# Inside WSL2:
# Verify GPU access (DO NOT install Linux NVIDIA drivers)
nvidia-smi
# Should show all 7 GPUs
```

### 1.2 DeepSpeed Distributed Training Setup
```bash
# Create virtual environment
python3.11 -m venv cybersec_moe_env
source cybersec_moe_env/bin/activate

# Install core dependencies
pip install torch==2.2.0+cu121 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install deepspeed==0.14.0
pip install transformers==4.40.0
pip install bitsandbytes==0.43.0
pip install peft==0.10.0
pip install accelerate==0.30.0

# Network configuration for distributed training
# Configure hostfile for DeepSpeed
cat > hostfile << EOF
master slots=1
worker1 slots=1
worker2 slots=1
worker3 slots=1
worker4 slots=1
worker5 slots=1
worker6 slots=1
EOF
```

### 1.3 Create MCP Server Infrastructure
```python
# mcp_security_server.py
import asyncio
from mcp import Server, Tool
from typing import Dict, List, Any

class CybersecurityMCPServer:
    def __init__(self):
        self.tools = {
            "burp_suite": BurpSuiteConnector(),
            "nmap": NmapConnector(),
            "shodan": ShodanAPIConnector(),
            "virustotal": VirusTotalConnector(),
            "misp": MISPConnector(),
            "neo4j": Neo4jThreatGraph(),
            "kafka": KafkaStreamProcessor()
        }
    
    async def handle_tool_request(self, tool_name: str, params: Dict) -> Any:
        """Route MCP requests to appropriate security tools"""
        return await self.tools[tool_name].execute(params)
```

## Phase 2: Data Collection & Processing

### 2.1 Create Comprehensive Data Collection Pipeline
```python
# data_collection_pipeline.py
import asyncio
from datetime import datetime
import json
from typing import List, Dict

class CyberKillChainDataCollector:
    def __init__(self):
        self.phases = {
            "reconnaissance": ReconDataCollector(),
            "weaponization": WeaponizationDataCollector(),
            "delivery": DeliveryDataCollector(),
            "exploitation": ExploitationDataCollector(),
            "installation": InstallationDataCollector(),
            "c2": C2DataCollector(),
            "exfiltration": ExfiltrationDataCollector()
        }
    
    async def collect_phase_data(self, phase: str) -> Dict:
        """Collect data for specific kill chain phase"""
        collectors = {
            "reconnaissance": self._collect_osint_data,
            "weaponization": self._collect_cve_exploits,
            "delivery": self._collect_phishing_data,
            "exploitation": self._collect_privilege_escalation,
            "installation": self._collect_malware_samples,
            "c2": self._collect_c2_traffic,
            "exfiltration": self._collect_data_theft_patterns
        }
        return await collectors[phase]()
    
    async def _collect_osint_data(self):
        """Collect OSINT data from multiple sources"""
        sources = [
            "https://api.shodan.io/",
            "https://otx.alienvault.com/api/v1/",
            "https://api.recordedfuture.com/",
            "https://api.github.com/advisories"
        ]
        # Implement parallel collection with rate limiting
        pass
```

### 2.2 CVE and Exploit Database Integration
```python
# cve_exploit_collector.py
async def collect_cve_data():
    """Collect CVE data with PoC exploits"""
    
    # NVD API v3 integration
    nvd_api = "https://services.nvd.nist.gov/rest/json/cves/2.0"
    
    # VulnCheck enhanced data
    vulncheck_api = "https://api.vulncheck.com/v3/"
    
    # GitHub Security Advisory
    github_api = "https://api.github.com/graphql"
    
    # Exploit-DB GitLab
    exploitdb_api = "https://gitlab.com/exploit-database/exploitdb"
    
    # Parallel collection with MCP integration
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_nvd_cves(session, start_date="2024-01-01"),
            fetch_vulncheck_enhanced(session),
            search_github_pocs(session, "CVE-2024"),
            fetch_exploitdb_latest(session)
        ]
        results = await asyncio.gather(*tasks)
    
    return merge_and_deduplicate(results)
```

## Phase 3: Model Architecture Implementation

### 3.1 Security-Optimized MoE Architecture
```python
# security_moe_model.py
import torch
import torch.nn as nn
from transformers import AutoModel, AutoTokenizer
from peft import LoraConfig, get_peft_model

class CybersecurityMoE(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.config = config
        
        # Expert models for each kill chain phase
        self.experts = nn.ModuleDict({
            "reconnaissance": self._create_osint_expert(),
            "weaponization": self._create_exploit_expert(),
            "delivery": self._create_phishing_expert(),
            "exploitation": self._create_privesc_expert(),
            "installation": self._create_malware_expert(),
            "c2": self._create_c2_expert(),
            "exfiltration": self._create_exfil_expert()
        })
        
        # Router with security-aware gating
        self.router = SecurityAwareRouter(
            input_dim=768,
            num_experts=7,
            top_k=2,
            jitter_noise=0.01
        )
        
        # MCP integration layer
        self.mcp_interface = MCPIntegrationLayer()
    
    def _create_osint_expert(self):
        """BERT-based OSINT expert with Graph Attention"""
        model = AutoModel.from_pretrained("microsoft/codebert-base")
        
        # Apply LoRA for efficient fine-tuning
        lora_config = LoraConfig(
            r=16,
            lora_alpha=32,
            target_modules=["query", "value"],
            lora_dropout=0.1,
            bias="none",
            task_type="FEATURE_EXTRACTION"
        )
        
        return get_peft_model(model, lora_config)
```

### 3.2 Quantization Configuration
```python
# quantization_config.py
from transformers import BitsAndBytesConfig
import torch

def get_phase_specific_quantization(phase: str, vram_limit: int = 11):
    """Get optimized quantization config for each phase"""
    
    configs = {
        "reconnaissance": BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4"
        ),
        "weaponization": BitsAndBytesConfig(
            load_in_8bit=True,  # Higher precision for exploit generation
            llm_int8_threshold=6.0,
            llm_int8_has_fp16_weight=True
        ),
        "c2": BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_quant_type="fp4"
        )
    }
    
    return configs.get(phase, configs["reconnaissance"])
```

## Phase 4: Training Pipeline with MCP Integration

### 4.1 Distributed Training Script
```python
# distributed_training.py
import deepspeed
from deepspeed import DeepSpeedConfig
import torch.distributed as dist

def create_training_config():
    return {
        "train_batch_size": 32,
        "gradient_accumulation_steps": 8,
        "optimizer": {
            "type": "AdamW",
            "params": {
                "lr": 2e-5,
                "betas": [0.9, 0.999],
                "eps": 1e-8,
                "weight_decay": 0.01
            }
        },
        "scheduler": {
            "type": "WarmupLR",
            "params": {
                "warmup_min_lr": 0,
                "warmup_max_lr": 2e-5,
                "warmup_num_steps": 1000
            }
        },
        "zero_optimization": {
            "stage": 3,
            "offload_optimizer": {
                "device": "cpu",
                "pin_memory": True
            },
            "offload_param": {
                "device": "cpu",
                "pin_memory": True
            },
            "overlap_comm": True,
            "contiguous_gradients": True,
            "sub_group_size": 1e9,
            "reduce_bucket_size": 1e6,
            "stage3_prefetch_bucket_size": 1e6,
            "stage3_param_persistence_threshold": 1e6
        },
        "gradient_clipping": 1.0,
        "fp16": {
            "enabled": False
        },
        "bf16": {
            "enabled": True
        }
    }

# Launch distributed training
deepspeed --num_gpus=7 --hostfile=hostfile train_cybersec_moe.py \
    --deepspeed_config=ds_config.json \
    --model_name="cybersec-moe-v1" \
    --dataset_path="/data/cyber_kill_chain/" \
    --output_dir="/models/cybersec_moe/"
```

### 4.2 MCP-Enhanced Training Loop
```python
# mcp_training_loop.py
async def train_with_mcp_integration(model, train_loader, mcp_server):
    """Training loop with 50% MCP integration"""
    
    for epoch in range(num_epochs):
        for batch_idx, batch in enumerate(train_loader):
            # Standard forward pass
            outputs = model(batch['input_ids'])
            
            # MCP integration (50% of training)
            if batch_idx % 2 == 0:
                # Query external threat intelligence
                threat_context = await mcp_server.query_threat_intel(
                    batch['threat_indicators']
                )
                
                # Enhance model predictions
                enhanced_outputs = model.mcp_interface(
                    outputs, 
                    threat_context
                )
                
                # Write to ML database
                await mcp_server.write_to_ml_database({
                    'timestamp': datetime.now(),
                    'predictions': enhanced_outputs,
                    'threat_context': threat_context,
                    'model_version': model.version
                })
            
            # Compute loss and backpropagate
            loss = compute_security_aware_loss(outputs, batch['labels'])
            loss.backward()
            optimizer.step()
```

## Phase 5: Production Deployment

### 5.1 FastAPI Service with Security Features
```python
# cybersec_api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
from typing import List, Dict

app = FastAPI(title="Cybersecurity MoE API")

class ThreatAnalysisRequest(BaseModel):
    indicators: List[str]
    phase: str
    context: Dict
    
@app.post("/analyze_threat")
async def analyze_threat(request: ThreatAnalysisRequest):
    """Analyze threat using appropriate expert"""
    
    # Load quantized expert for the phase
    expert = load_quantized_expert(
        phase=request.phase,
        device="cuda:0"
    )
    
    # MCP tool integration
    mcp_results = await gather_mcp_intelligence(
        indicators=request.indicators,
        tools=["shodan", "virustotal", "misp"]
    )
    
    # Expert analysis
    analysis = expert.analyze(
        indicators=request.indicators,
        mcp_context=mcp_results
    )
    
    # Store in ML database
    await store_analysis_results(analysis)
    
    return {
        "threat_level": analysis.threat_level,
        "recommendations": analysis.recommendations,
        "iocs": analysis.extracted_iocs
    }
```

### 5.2 Monitoring and Continuous Updates
```python
# monitoring_pipeline.py
class ModelMonitoring:
    def __init__(self):
        self.metrics = {
            "false_positive_rate": [],
            "false_negative_rate": [],
            "detection_accuracy": [],
            "mcp_latency": [],
            "gpu_utilization": []
        }
    
    async def continuous_update_loop(self):
        """Weekly model updates with new threat intelligence"""
        while True:
            # Collect new threat data
            new_data = await collect_weekly_threats()
            
            # Fine-tune specific experts
            for phase, data in new_data.items():
                if len(data) > 1000:  # Threshold for retraining
                    await retrain_expert(phase, data)
            
            # Update model version
            await deploy_updated_model()
            
            # Wait for next update cycle
            await asyncio.sleep(7 * 24 * 60 * 60)  # 1 week
```

## Execution Instructions

1. **Initial Setup**: Run all Phase 1 commands to configure environment
2. **Data Collection**: Execute Phase 2 scripts to gather training data
3. **Model Creation**: Implement Phase 3 architecture with quantization
4. **Training**: Launch distributed training with MCP integration (Phase 4)
5. **Deployment**: Deploy API service and monitoring (Phase 5)

## Critical Configuration Notes

- Always use absolute paths in Docker/WSL2 environments
- Monitor VRAM usage (target: 10-11GB per GPU)
- Implement rate limiting for external APIs
- Use async/await for all MCP operations
- Enable gradient checkpointing for large models
- Validate security metrics before production deployment

**Remember**: Use ultrathinking for optimization decisions, employ parallel processing wherever possible, and maintain security-first architecture throughout implementation.