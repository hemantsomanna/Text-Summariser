from textsummariser.pipeline.stage1data_ingestion import DataIngestionTrainingPipeline
from textsummariser.logging import logger
from textsummariser.pipeline.stage2data_validation import DataValidationTrainingPipeline
from textsummariser.pipeline.stage3data_transformation import DataTransformationTrainingPipeline
from textsummariser.pipeline.stage4model_trainer import ModelTrainerTrainingPipeline

STAGE_NAME = "Model Trainer stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainerTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e