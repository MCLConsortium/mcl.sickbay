# encoding: utf-8

'''
🤢 Sickbay: Clinical data model for the Consortium for Molecular and Cellular
Characterization of Screen-Detected Lesions.

JSON utilities. These are classes that can be passed to ``json.dump(cls=)``.
'''

from .model import (
    Biospecimen,
    BreastOrgan,
    ClinicalCore,
    Genomics,
    Imaging,
    LabCASMetadata,
    LungOrgan,
    Organ,
    PancreasOrgan,
    ProstateOrgan,
    Smart3SeqGenomics,
)
import json, datetime, enum


class SickbayEncoder(json.JSONEncoder):
    '''Generic encoder for everything in the Consortium for Molecular and Cellular
    Characterization of Screen-Detected Lesions Sickbay.
    '''
    def default(self, obj):
        '''See https://docs.python.org/3/library/json.html#json.JSONEncoder.default'''
        if isinstance(obj, datetime.date):
            return (obj.year, obj.month, obj.day)
        elif isinstance(obj, enum.Enum):
            return obj.name  # 🤔 Should this return the enumeration's name or value? Guess we'll do name for now
        else:
            return super(SickbayEncoder, self).default(obj)
    def addAttributes(self, obj, attrNames, d):
        '''Add all the attributes named in ``attrNames`` to the dictionary ``d`` with values from
        ``obj``. If an attribute is unset or ``None``, just omit it. If an attribute value is an
        enumerated type, use the enumeration name and its value as 2-entry dicts with the
        ``label`` equal to the value and the ``token`` equal to the name.
        '''
        for name in attrNames:
            value = getattr(obj, name, None)
            if value is not None:
                if isinstance(value, enum.Enum):
                    d[name] = dict(label=value.value, token=value.name)
                else:
                    d[name] = value


class LabCASMetadataEncoder(SickbayEncoder):
    def default(self, obj):
        '''See https://docs.python.org/3/library/json.html#json.JSONEncoder.default'''
        if isinstance(obj, LabCASMetadata):
            # Add a "tag" to indicate the "class", and the labcasID which is non-nullable
            d = {
                f'__{obj.__class__.__module__}.{obj.__class__.__name__}__': True,
                'labcasID': obj.labcasID
            }

            # These other attributes are nullable
            nullableAttributes = (
                'fileName', 'siteID', 'submittingInvestigatorID', 'processingLevel', 'fileType',
                'consortium', 'protocolID', 'dateFileGenerated'
            )
            self.addAttributes(obj, nullableAttributes, d)
            return d
        else:
            return super(LabCASMetadataEncoder, self).default(obj)


class OrganEncoder(LabCASMetadataEncoder):
    def default(self, obj):
        '''See https://docs.python.org/3/library/json.html#json.JSONEncoder.default'''
        if isinstance(obj, Organ):
            d = super(OrganEncoder, self).default(obj)
            d['identifier'] = obj.identifier
            d['organType'] = obj.organType
            if obj.histopathology_precancer_types is not None and len(obj.histopathology_precancer_types) > 0:
                # 🤔 Should this return the enumeration's name or value? Guess we'll do name for now
                d['histopathology_precancer_types'] = [i.hp_type.name for i in obj.histopathology_precancer_types]
            return d
        else:
            return super(OrganEncoder, self).default(obj)


class BreastOrganEncoder(OrganEncoder):
    _breastAttributes = (
        'anchor_type', 'grade', 'laterality', 'site', 'size', 'necrosis', 'necrosis_location', 'surgical_margin',
        'recurrence', 'pathologic_T_stage_7', 'pathologic_N_stage_7', 'pathologic_M_stage_7', 'clinical_T_stage_7',
        'clinical_N_stage_7', 'clinical_M_stage_7', 'disease_stage_7', 'path_TNM_class_T_8', 'path_TNM_class_M_8',
        'clinical_TNM_class_T_8', 'clinical_TNM_class_N_8', 'clinical_TNM_class_M_8', 'disease_stage_ajcc_8',
        'genetic_testing', 'brca1', 'brca2', 'estrogen_receptor', 'er_percent_positivity', 'progesterone_receptor',
        'her2_immunohistochemistry', 'her2_in_situ_hybridization', 'ki_67_percent_positive_nuclei',
        'menopausal_status', 'ecog_score', 'method_of_detection', 'days_to_detection_date',
        'days_to_last_screening_mammo', 'days_to_last_negative_screening_mammo', 'detected_between_screening_intervals',
        'multifocal_disease', 'multicentric_disease', 'imaging_workup', 'birads_density',
    )
    def default(self, obj):
        '''See https://docs.python.org/3/library/json.html#json.JSONEncoder.default'''
        if isinstance(obj, BreastOrgan):
            d = super(BreastOrganEncoder, self).default(obj)
            self.addAttributes(obj, self._breastAttributes, d)
            return d
        else:
            return super(BreastOrganEncoder, self).default(obj)


class ProstateOrganEncoder(OrganEncoder):
    _prostateAttributes = (
        'histologic_type', 'histologic_subtype', 'morphologic_cytologic_subtypes',
        'morphologic_cytologic_subcategories', 'gleason_score_dominant_nodule', 'gleason_grade_group',
        'percent_gleason_pattern_4', 'tumor_extent', 'location_dominant_nodule', 'location_secondary_nodule',
        'local_extent', 'location_extent_extraprostatic_extension', 'margins', 'location_nature_positive_margins',
        'summed_length_positive_margin', 'highest_grade_at_margin', 'seminal_vesicle_invasion',
        'lymphatic_invasion', 'pelvic_lymph_nodes', 'tumor_in_pelvic_lymph_nodes', 'lymph_nodes_metastatic_carcinoma',
        'lymph_nodes_tested', 'lymph_node_location', 'extranodal_extension_identified',
        'ajcc_extent_of_invasion_primary_tumor', 'ajcc_extent_of_invasion_regional_lymph_nodes',
        'ajcc_extent_of_invasion_summary_margins', 'ajcc_staging_system_edition', 'ajcc_clinical_m',
        'ajcc_clinical_n', 'ajcc_clinical_t', 'ajcc_clinical_stage', 'ajcc_pathologic_m', 'ajcc_pathologic_n',
        'ajcc_pathologic_t', 'ajcc_pathologic_stage', 'additonal_findings_uninvolved_prostate',
        'prior_malignancy', 'prior_treatment'
    )
    def default(self, obj):
        '''See https://docs.python.org/3/library/json.html#json.JSONEncoder.default'''
        if isinstance(obj, ProstateOrgan):
            d = super(ProstateOrganEncoder, self).default(obj)
            self.addAttributes(obj, self._prostateAttributes, d)
            return d
        else:
            return super(ProstateOrganEncoder, self).default(obj)


class LungOrganEncoder(OrganEncoder):
    _lungAttributes = (
        'histopathology_precancer_type', 'histopathology_precancer_type_other', 'collection_method',
        'lymphocytes', 'neutrophils', 'plasma_cells', 'macrophages', 'lung_location', 'lobe_bronchial_location',
        'segment', 'branch', 'histologic_type', 'primary_adenocarcinoma_differentiation_type', 'tumor_grade',
        'ajcc_staging_system_edition', 'ajcc_clinical_m', 'ajcc_clinical_n', 'ajcc_clinical_t', 'ajcc_clinical_stage',
        'ajcc_pathologic_m', 'ajcc_pathologic_n', 'ajcc_pathologic_t', 'ajcc_pathologic_stage', 'lymph_nodes_tested',
        'lymph_nodes_positive', 'prior_malignancy', 'prior_treatment'
    )
    def default(self, obj):
        '''See https://docs.python.org/3/library/json.html#json.JSONEncoder.default'''
        if isinstance(obj, LungOrgan):
            d = super(LungOrganEncoder, self).default(obj)
            self.addAttributes(obj, self._lungAttributes, d)
            return d
        else:
            return super(LungOrganEncoder, self).default(obj)


class PancreasOrganEncoder(OrganEncoder):
    _pancreasAttributes = (
        'histological_grading', 'histological_subtypes_ipmn', 'tumor_pathology_location', 'lesion_focality',
        'number_lesions', 'mitotic_rate', 'necrosis', 'path_number_of_tumors', 'path_tumor_size_largest_lesion',
        'lesion_size', 'path_ipmn_grade_at_excision', 'final_path_duct_communication', 'path_management_recommendation',
        'path_acc_num_diag_biopsy', 'path_immunohistochemistry', 'path_immunohistochemistry_outcome',
        'histology_grading', 'exocrine_pathologic_T_AJCC_8', 'exocrine_pathologic_N_AJCC_8',
        'exocrine_pathologic_M_AJCC_8', 'exocrine_clinical_T_AJCC_8', 'exocrine_clinical_N_AJCC_8',
        'exocrine_clinical_M_AJCC_8', 'exocrine_group_stage_AJCC_8', 'neuroendocrine_pathologic_T_AJCC_8',
        'neuroendocrine_pathologic_N_AJCC_8', 'neuroendocrine_pathologic_M_AJCC_8',
        'neuroendocrine_clinical_T_AJCC_8', 'neuroendocrine_clinical_N_AJCC_8',
        'neuroendocrine_clinical_M_AJCC_8', 'neuroendocrine_group_stage'
    )
    def default(self, obj):
        '''See https://docs.python.org/3/library/json.html#json.JSONEncoder.default'''
        if isinstance(obj, PancreasOrgan):
            d = super(PancreasOrganEncoder, self).default(obj)
            self.addAttributes(obj, self._pancreasAttributes, d)
            return d
        else:
            return super(PancreasOrganEncoder, self).default(obj)


ORGAN_ENCODERS = {
    Organ: OrganEncoder,  # https://github.com/MCLConsortium/mcl.sickbay/issues/12
    BreastOrgan: BreastOrganEncoder,
    ProstateOrgan: ProstateOrganEncoder,
    LungOrgan: LungOrganEncoder,
    PancreasOrgan: PancreasOrganEncoder,
    # Additional encoders here as additional organs come to be
}


class GenomicsEncoder(LabCASMetadataEncoder):
    _genomicsAttributes = (
        'sequencing_center', 'sequencing_batch_id', 'library_name', 'library_strategy',
        'library_source', 'library_selection', 'library_strand', 'library_layout', 'sequencing_platform',
        'read_length', 'rin', 'adapter_name', 'adapter_sequence', 'flow_cell_barcode', 'size_selection_range',
        'target_capture_kit_target_region',
    )
    def default(self, obj):
        '''See https://docs.python.org/3/library/json.html#json.JSONEncoder.default'''
        if isinstance(obj, Genomics):
            d = super(GenomicsEncoder, self).default(obj)
            d['specimen_ID'] = obj.specimen_ID
            when = obj.sequencing_date
            d['sequencing_date'] = (when.year, when.month, when.day)
            self.addAttributes(obj, self._genomicsAttributes, d)
            return d
        else:
            return super(GenomicsEncoder, self).default(obj)


class Smart3SeqGenomicsEncoder(GenomicsEncoder):
    _smart3SeqGenomicsAttributes = (
        'input_type', 'number_PCR_cycles', 'number_libraries_in_pool', 'index_sequence', 'indexing_type',
        'indexing_type_other',
    )
    def default(self, obj):
        '''See https://docs.python.org/3/library/json.html#json.JSONEncoder.default'''
        if isinstance(obj, Smart3SeqGenomics):
            d = super(Smart3SeqGenomicsEncoder, self).default(obj)
            self.addAttributes(obj, self._smart3SeqGenomicsAttributes, d)
            return d
        else:
            return super(Smart3SeqGenomicsEncoder, self).default(obj)


GENOMICS_ENCODERS = {
    Genomics: GenomicsEncoder,
    Smart3SeqGenomics: Smart3SeqGenomicsEncoder,
    # Additional encoders here as additional genomics come to be
}


class ClinicalCoreEncoder(LabCASMetadataEncoder):
    _clinicalCoreAttributes = (
        'anchor_type', 'year_of_birth', 'age_at_index', 'height', 'days_to_weight_recorded', 'weight',
        'days_to_diagnosis', 'year_of_diagnosis', 'age_at_diagnosis',
        'days_to_detection_date', 'days_to_last_screen_date', 'days_to_last_neg_screen_date', 'gender',
        'ethnicity', 'race', 'education', 'income', 'prior_cancer', 'current_lesion_type', 'how_detected',
        'mode_of_detection', 'lesion_type', 'specimen_collected', 'biomarker_tested',
        'relative_with_cancer_history', 'tobacco_smoking_status', 'type_tobacco_used', 'alcohol_history',
        'days_to_consent', 'days_to_enrollment', 'vital_status', 'days_to_vital_status_reference',
        'days_to_birth', 'age_at_menses_start', 'menses_stop', 'age_at_menses_stop',
        'relative_with_cancer_history_count', 'tobacco_smoking_onset_age', 'tobacco_smoking_quit_age',
        'years_smoked', 'cigarettes_per_day', 'alcohol_drinks_per_day', 'alcohol_days_per_week'
    )
    def default(self, obj):
        '''See https://docs.python.org/3/library/json.html#json.JSONEncoder.default'''
        if isinstance(obj, ClinicalCore):
            d = super(ClinicalCoreEncoder, self).default(obj)
            d['participant_ID'] = obj.participant_ID
            self.addAttributes(obj, self._clinicalCoreAttributes, d)
            if obj.prior_lesions is not None and len(obj.prior_lesions) > 0:
                # 🤔 Should this return the enumeration's name or value? Guess we'll do name for now
                d['prior_lesions'] = [i.lesion_type.name for i in obj.prior_lesions]
            if obj.core_races is not None and len(obj.core_races) > 0:
                # 🤔 Ditto
                d['core_races'] = [i.race.name for i in obj.core_races]
            if obj.core_tobaccos is not None and len(obj.core_tobaccos) > 0:
                d['core_tobaccos'] = [i.type_tobacco_used.name for i in obj.core_tobaccos]
            if obj.biospecimens:
                e = BiospecimenEncoder()
                d['biospecimens'] = [e.default(i) for i in obj.biospecimens]
            if obj.genomics:
                d['genomics'] = [GENOMICS_ENCODERS[i.__class__]().default(i) for i in obj.genomics]
            if obj.images:
                e = ImagingEncoder()
                d['images'] = [e.default(i) for i in obj.images]
            if obj.organs:
                d['organs'] = [ORGAN_ENCODERS[i.__class__]().default(i) for i in obj.organs]
            return d
        else:
            return super(ClinicalCoreEncoder, self).default(obj)


class BiospecimenEncoder(LabCASMetadataEncoder):
    _biospecimenAttributes = (
        'specimen_ID_local', 'specimen_parent_ID', 'specimen_type', 'anatomical_site', 'tumor_tissue_type',
        'precancer_type', 'precancer_type_other', 'specimen_laterality', 'acquisition_method',
        'acquisition_method_other', 'days_to_collection', 'time_excision_to_processing', 'ischemic_time',
        'portion_weight', 'total_volume', 'preservation_method', 'preservation_method_other', 'fixative_used',
        'fixatives_other', 'fixation_duration', 'processing_duration', 'analyte_type', 'analyte_type_other',
        'protocol_number', 'protocol_version', 'storage_method', 'storage_method_other', 'days_to_storage',
        'slide_charge_type', 'section_thickness', 'days_to_shipping', 'shipping_conditions', 'shipping_destination'
    )
    def default(self, obj):
        '''See https://docs.python.org/3/library/json.html#json.JSONEncoder.default'''
        if isinstance(obj, Biospecimen):
            d = super(BiospecimenEncoder, self).default(obj)
            d['specimen_ID'] = obj.specimen_ID
            self.addAttributes(obj, self._biospecimenAttributes, d)
            if obj.adjacent_specimens:
                d['adjacent_specimens'] = [i.adjacent_specimen_ID for i in obj.adjacent_specimens]
            if obj.genomics:
                d['genomics'] = [GENOMICS_ENCODERS[i.__class__]().default(i) for i in obj.genomics]
            if obj.images:
                e = ImagingEncoder()
                d['images'] = [e.default(i) for i in obj.images]
            return d
        else:
            return super(BiospecimenEncoder, self).default(obj)


class ImagingEncoder(LabCASMetadataEncoder):
    _imagingAttributes = ('some_attribute',)
    def default(self, obj):
        '''See https://docs.python.org/3/library/json.html#json.JSONEncoder.default'''
        if isinstance(obj, Imaging):
            d = super(ImagingEncoder, self).default(obj)
            d['identifier'] = obj.identifier
            self.addAttributes(obj, self._imagingAttributes, d)
            return d
        else:
            return super(ImagingEncoder, self).default(obj)
