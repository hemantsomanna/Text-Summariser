from textsummariser.pipeline.stage1data_ingestion import DataIngestionTrainingPipeline
from textsummariser.logging import logger
from textsummariser.pipeline.stage2data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data Validation Stage"
try:
    logger.info({STAGE_NAME})
    data_validation = DataValidationTrainingPipeline()
    data_validation .main()
    logger.info("COMPLETED")
except Exception as e:
        logger.exception(e)
        raise e 